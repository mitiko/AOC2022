use std::{fs, collections::VecDeque};
use hashbrown::HashSet;

// ore, clay, obsidian, geode
#[derive(Debug, Clone, Hash, PartialEq, Eq)]
struct Minerals(u16, u16, u16, u16);

#[derive(Debug, Clone, Hash, PartialEq, Eq)]
struct State {
    materials: Minerals,
    production: Minerals,
    minute: u16
}

impl State {
    fn earn(&mut self) {
        self.materials.0 += self.production.0;
        self.materials.1 += self.production.1;
        self.materials.2 += self.production.2;
        self.materials.3 += self.production.3;
    }
}

#[derive(Debug)]
struct Blueprint {
    ore: u16,
    clay: u16,
    obsidian: (u16, u16),
    geode: (u16, u16)
}

fn main() {
    let input = fs::read_to_string("input.txt").unwrap();
    use regex::Regex;
    let re = Regex::new(r"\d+").unwrap();
    let mut blueprints = Vec::new();

    for line in input.lines() {
        let matches: Vec<u16> = re.find_iter(line)
            .skip(1)
            .map(|x| x.as_str())
            .map(|x| u16::from_str_radix(x, 10).unwrap())
            .collect();

        blueprints.push(Blueprint {
            ore: matches[0], clay: matches[1],
            obsidian: (matches[2], matches[3]),
            geode: (matches[4], matches[5])
        });
    }

    let mut total = 1;
    for b in blueprints.iter().take(3) {
        total *= mine(b) as u64;
    }
    println!("{}", total);
}

fn mine(b: &Blueprint) -> u16 {
    let initial = State {
        materials: Minerals(0, 0, 0, 0),
        production: Minerals(1, 0, 0, 0),
        minute: 32
    };
    let max_ore = [b.ore, b.clay, b.obsidian.0, b.geode.0].into_iter().max().unwrap();
    let max_clay = b.obsidian.1;
    let max_obsidian = b.geode.1;
    let mut ans = 0;
    
    let mut bfs = VecDeque::from([initial]);
    let mut seen = HashSet::new();

    while let Some(mut state) = bfs.pop_front() {
        if seen.contains(&state) { continue; }
        else { seen.insert(state.clone()); }

        if state.minute == 0 {
            ans = std::cmp::max(ans, state.materials.3);
            continue;
        }

        let prev = state.clone();
        state.earn();
        state.minute -= 1;

        // geode
        if prev.materials.2 >= b.geode.1 && prev.materials.0 >= b.geode.0 {
            let mut s = state.clone();
            s.materials.0 -= b.geode.0;
            s.materials.2 -= b.geode.1;
            s.production.3 += 1;
            bfs.push_back(s);
            continue;
        }
        
        // obsidian
        if prev.production.2 < max_obsidian && prev.materials.1 >= b.obsidian.1 && prev.materials.0 >= b.obsidian.0 {
            let mut s = state.clone();
            s.materials.0 -= b.obsidian.0;
            s.materials.1 -= b.obsidian.1;
            s.production.2 += 1;
            bfs.push_back(s);
            continue;
        }

        // ore
        if prev.production.0 < max_ore && prev.materials.0 >= b.ore {
            let mut s = state.clone();
            s.materials.0 -= b.ore;
            s.production.0 += 1;
            bfs.push_back(s);
        }

        // clay
        if prev.production.1 < max_clay && prev.materials.0 >= b.clay {
            let mut s = state.clone();
            s.materials.0 -= b.clay;
            s.production.1 += 1;
            bfs.push_back(s);
        }

        bfs.push_back(state);
    }
    ans
}
